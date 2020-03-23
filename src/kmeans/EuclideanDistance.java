package kmeans;

import java.util.Map;

/**
 * The type Euclidean distance.
 * <p>
 * Defines how we calculate the Euclidean distance between two feature lists.
 *
 * @author maw101
 * @version 1.0
 */
public class EuclideanDistance implements Distance {

   /**
    * Calculates the Euclidean distance between two feature lists.
    *
    * @param featureSetOne the first feature list
    * @param featureSetTwo the second feature list
    * @return the Euclidean distance between the two feature lists
    */
   @Override
   public double calc(Map<String, Double> featureSetOne, Map<String, Double> featureSetTwo) {
      double distanceSum = 0.0;
      // for each feature, add the distance between feature sets to the overall sum
      for (String key : featureSetOne.keySet()) {
         Double featureSetOneValue = featureSetOne.get(key);
         Double featureSetTwoValue = featureSetTwo.get(key);

         if (featureSetOneValue != null && featureSetTwoValue != null) {
            distanceSum += Math.pow((featureSetOneValue - featureSetTwoValue), 2);
         }
      }

      // return the distance between both feature lists
      return Math.sqrt(distanceSum);
   }

}
