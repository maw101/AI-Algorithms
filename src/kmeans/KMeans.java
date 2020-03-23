package kmeans;

import java.util.*;
import java.util.stream.Collectors;

/**
 * An implementation of the K-Means Algorithm.
 * <p>
 * Provides methods to perform K-Means on a set of data records given a set of
 * starting centroids, a given k, and a distance calculation method. No
 * restriction on the number of dimensions data record features have.
 *
 * @author maw101
 * @version 1.0
 */
public class KMeans {

   /**
    * Perform the K-Means Algorithm on a set of data records.
    * <p>
    * Requires a list of starting centroids, a k value and a distance
    * calculation method.
    *
    * @param dataRecords       a list of data records
    * @param startingCentroids the starting centroids
    * @param k                 the k value for K-Means
    * @param distanceMethod    the distance calculation method
    *
    * @return a map of centroids mapping to a list of data records
    */
   public static Map<Centroid, List<DataRecord>> perform(List<DataRecord> dataRecords, List<Centroid> startingCentroids, int k, Distance distanceMethod) {
      System.out.println("====== PERFORMING K-MEANS ======");

      List<Centroid> centroids = startingCentroids;
      Map<Centroid, List<DataRecord>> currentClusters;
      Map<Centroid, List<DataRecord>> previousClusters = new HashMap<>();

      do {
         currentClusters = new HashMap<>();

         for (DataRecord record : dataRecords) {
            // 1. computer distance from all data points to all k centroids to determine nearest
            Centroid nearestCentroid = locateNearestCentroid(record, distanceMethod, centroids);
            // 2. assign data point to the cluster whose current centroid is nearest
            assignRecordToCluster(currentClusters, record, nearestCentroid);
         }

         // check to see if our clusters have remained the same
         if (currentClusters == previousClusters) {
            break;
         }

         previousClusters = currentClusters;
         // 3. for each centroid, compute the average of all points assigned to it
         for (int i = 0; i < centroids.size(); i++) {
            Centroid currentCentroid = centroids.get(i);
            Map<String, Double> clusterAverages = getClusterAverage(currentCentroid, currentClusters.get(currentCentroid));
            // 4. replace centroid with new averages
            centroids.set(i, new Centroid(clusterAverages));
         }

         System.out.println("Previous Clusters: ");
         printClusterCollectionSummary(previousClusters);

         System.out.println("Current Clusters: ");
         printClusterCollectionSummary(currentClusters);

      } while (currentClusters != previousClusters);

      System.out.println("FINAL Clusters: ");
      printClusterCollectionSummary(currentClusters);

      return currentClusters;
   }

   /**
    * Locate the nearest centroid to a data record.
    *
    * @param record         the data record
    * @param distanceMethod the distance calculation method
    * @param centroids      a list of centroids
    *
    * @return the nearest centroid to the data record
    */
   private static Centroid locateNearestCentroid(DataRecord record, Distance distanceMethod, List<Centroid> centroids) {
      double lowestDistance = Double.MAX_VALUE;
      Centroid nearestCentroid = null;

      // for each centroid, determine distance to each record
      for (Centroid centroid : centroids) {
         double distance = distanceMethod.calc(record.getFeatures(), centroid.getCoordinates());

         if (distance < lowestDistance) {
            // update closest centroid
            nearestCentroid = centroid;
            lowestDistance = distance;
         }
      }

      return nearestCentroid;
   }

   /**
    * Assign a record to a given cluster.
    *
    * @param clusters        a map of clusters
    * @param record          the data record
    * @param nearestCentroid the nearest centroid to the data record
    */
   private static void assignRecordToCluster(Map<Centroid, List<DataRecord>> clusters, DataRecord record, Centroid nearestCentroid) {
      List<DataRecord> currentCentroidList = clusters.get(nearestCentroid);

      if (currentCentroidList == null) {
         currentCentroidList = new ArrayList<>();
      }

      currentCentroidList.add(record);

      clusters.put(nearestCentroid, currentCentroidList);
   }

   /**
    * Gets cluster average from each feature.
    *
    * @param centroid the centroid of the cluster to get the average for
    * @param records  a list of data records
    *
    * @return the cluster average
    */
   private static Map<String, Double> getClusterAverage(Centroid centroid, List<DataRecord> records) {
      if ((records == null) || records.isEmpty()) {
         return centroid.getCoordinates();
      }

      // get a map of the correct dimension (number of features)
      Map<String, Double> averages = centroid.getCoordinates();
      // set the identifier for each feature and set average to zero
      Set<String> featureNames = records.get(0).getFeatures().keySet();
      for (String featureName : featureNames) {
         averages.put(featureName, 0.0);
      }

      // for each record, compute the average for each feature
      for (DataRecord record : records) {
         // for each feature, get the value, and add this to the current sum for the feature in 'averages'
         record.getFeatures().forEach(
                 (featureName, featureValue) -> averages.compute(
                         featureName, (averagesFeatureName, currentSum) -> featureValue + currentSum
                 )
         );
      }

      // find the average for each feature, currently just the sum
      int recordCount = records.size();
      averages.forEach(
              (featureName, featureSum) -> averages.put(featureName, (featureSum / recordCount))
      );

      return averages;
   }

   /**
    * Print cluster collection summary.
    * <p>
    * For each cluster, prints the summary for it.
    *
    * @param clusters the clusters
    */
   public static void printClusterCollectionSummary(Map<Centroid, List<DataRecord>> clusters) {
      System.out.println();
      clusters.forEach(
              ((centroid, dataRecords) -> System.out.println(getClusterSummary(centroid, dataRecords)))
      );
      System.out.println();
   }

   /**
    * Gets cluster summary.
    *
    * @param centroid the centroid of the cluster to get the summary for
    * @param records  a list of data records
    *
    * @return a string representation of the cluster summary
    */
   public static String getClusterSummary(Centroid centroid, List<DataRecord> records) {
      StringBuilder str = new StringBuilder(centroid.toString());
      str.append(" Record Identifiers: ");
      str.append((records.stream()
              .map(key -> key.getIdentifier())
              .collect(Collectors.joining(", ", "[", "]"))));
      return str.toString();
   }

}