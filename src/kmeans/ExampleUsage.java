package kmeans;

import java.util.*;

/**
 * An example application to show usage of the KMeans class.
 *
 * @author maw101
 * @version 1.0
 * @since 1.0
 */
public class ExampleUsage {

   /**
    * The entry point of the application.
    *
    * @param args the input arguments
    */
   public static void main(String[] args) {
      exampleOneDimensional();
      //exampleTwoDimensional();
   }

   /**
    * Performs K-Means on a One Dimensional data set.
    * <p>
    * Constructs an example set of 1-D data records, creates example centroids
    * and performs K-Means on these data.
    */
   private static void exampleOneDimensional() {
      Map<String, Double> tempFeatureMap;
      // create example data records
         double[] values = new double[]{6, 8, 18, 26, 13, 32, 24};
         List<DataRecord> dataRecords = new ArrayList<>();

         // add each data record in turn
         for (int i = 0; i < values.length; i++) {
            tempFeatureMap = new HashMap<>(
                    Map.ofEntries(
                            new AbstractMap.SimpleEntry<>("value", values[i])
                    )
            );

            dataRecords.add(new DataRecord(String.valueOf(values[i]), tempFeatureMap));

            System.out.println(dataRecords.get(i));
         }

      // create example centroids
         double[] initialCentroidValues = new double[]{11, 20};
         List<Centroid> startingCentroids = new ArrayList<>();

         // add each centroid in turn
         for (Double initialCentroidValue : initialCentroidValues) {
            tempFeatureMap = new HashMap<>(
                    Map.ofEntries(
                            new AbstractMap.SimpleEntry<>("value", initialCentroidValue)
                    )
            );

            startingCentroids.add(new Centroid(tempFeatureMap));
         }

      // set k value for k-means
         int k = 2;

      KMeans.perform(dataRecords, startingCentroids, k, new EuclideanDistance());
   }

   /**
    * Performs K-Means on a Two Dimensional data set.
    * <p>
    * Constructs an example set of 2-D data records, creates example centroids
    * and performs K-Means on these data.
    */
   private static void exampleTwoDimensional() {
      // using data from: https://www.youtube.com/watch?v=wt-X61BnUCA

      Map<String, Double> tempFeatureMap;
      // create example data records
      double[][] values = new double[][]{{185, 72}, {170, 56}, {168, 60}, {179, 68}, {182, 72}, {188, 77}};
      List<DataRecord> dataRecords = new ArrayList<>();

      // add each data record in turn
      for (int i = 1; i <= values.length; i++) {
         tempFeatureMap = new HashMap<>(
                 Map.ofEntries(
                         new AbstractMap.SimpleEntry<>("X", values[i-1][0]),
                         new AbstractMap.SimpleEntry<>("Y", values[i-1][1])
                 )
         );

         dataRecords.add(new DataRecord(String.valueOf(i), tempFeatureMap));

         System.out.println(dataRecords.get(i-1));
      }

      // create example centroids
      double[][] initialCentroidValues = new double[][]{{185, 72}, {170, 56}};
      List<Centroid> startingCentroids = new ArrayList<>();

      // add each centroid in turn
      for (int i = 0; i < initialCentroidValues.length; i++) {
         tempFeatureMap = new HashMap<>(
                 Map.ofEntries(
                         new AbstractMap.SimpleEntry<>("X", initialCentroidValues[i][0]),
                         new AbstractMap.SimpleEntry<>("Y", initialCentroidValues[i][1])
                 )
         );

         startingCentroids.add(new Centroid(tempFeatureMap));
      }

      // set k value for k-means
      int k = 2;

      KMeans.perform(dataRecords, startingCentroids, k, new EuclideanDistance());
   }

}