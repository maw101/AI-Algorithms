package kmeans;

import java.util.Map;

/**
 * The interface Distance.
 * <p>
 * Defines an interface for measuring distances between two feature lists.
 *
 * @author maw101
 * @version 1.0
 */
public interface Distance {

   /**
    * Calculates the distance between two feature lists.
    *
    * @param featureOne the first feature list
    * @param featureTwo the second feature list
    * @return the distance between the two feature lists
    */
   double calc(Map<String, Double> featureOne, Map<String, Double> featureTwo);

}