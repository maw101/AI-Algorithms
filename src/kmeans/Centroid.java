package kmeans;

import java.util.Map;
import java.util.Objects;
import java.util.stream.Collectors;

/**
 * The type Centroid.
 * <p>
 * Centre of all the data points belonging to a cluster.
 *
 * @author maw101
 * @version 1.0
 */
public class Centroid {

   private Map<String, Double> coordinates;

   /**
    * Instantiates a new Centroid.
    *
    * @param coordinates the coordinates
    */
   public Centroid(Map<String, Double> coordinates) {
      this.coordinates = coordinates;
   }

   /**
    * Gets coordinates.
    *
    * @return the coordinates
    */
   public Map<String, Double> getCoordinates() {
      return coordinates;
   }

   /**
    * Sets coordinates.
    *
    * @param coordinates the coordinates
    */
   public void setCoordinates(Map<String, Double> coordinates) {
      this.coordinates = coordinates;
   }

   /**
    * Returns a string representation of the centroid.
    *
    * @return a string representation of the centroid.
    */
   @Override
   public String toString() {
      return "Centroid " +
              coordinates.keySet().stream()
              .map(key -> key + "=" + coordinates.get(key))
              .collect(Collectors.joining(", ", "(", ")"));
   }

   /**
    * Indicates whether some other object is "equal to" this one.
    *
    * @param o the reference object with which to compare
    *
    * @return  true if this object is the same as the object argument;
    *          false otherwise.
    */
   @Override
   public boolean equals(Object o) {
      if (this == o) return true;
      if (o == null || getClass() != o.getClass()) return false;
      Centroid centroid = (Centroid) o;
      return Objects.equals(coordinates, centroid.coordinates);
   }

   /**
    * Returns a hash code value for the object.
    *
    * @return a hash code value for this object.
    */
   @Override
   public int hashCode() {
      return Objects.hash(coordinates);
   }

}