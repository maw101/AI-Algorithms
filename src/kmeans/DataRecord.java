package kmeans;

import java.util.Map;

/**
 * The type Data record.
 * <p>
 * Holds a data record consisting of a record identifier and a number of
 * named features (columns).
 *
 * @author maw101
 * @version 1.0
 */
public class DataRecord {

   private String identifier;
   private Map<String, Double> features;

   /**
    * Instantiates a new Data record.
    *
    * @param identifier the identifier
    * @param features   the features
    */
   public DataRecord(String identifier, Map<String, Double> features) {
      this.identifier = identifier;
      this.features = features;
   }

   /**
    * Gets identifier.
    *
    * @return the identifier
    */
   public String getIdentifier() {
      return identifier;
   }

   /**
    * Sets identifier.
    *
    * @param identifier the identifier
    */
   public void setIdentifier(String identifier) {
      this.identifier = identifier;
   }

   /**
    * Gets features.
    *
    * @return the features
    */
   public Map<String, Double> getFeatures() {
      return features;
   }

   /**
    * Sets features.
    *
    * @param features the features
    */
   public void setFeatures(Map<String, Double> features) {
      this.features = features;
   }

   /**
    * Returns a string representation of the data record.
    *
    * @return a string representation of the data record.
    */
   @Override
   public String toString() {
      return "DataRecord{" +
              "identifier='" + identifier + '\'' +
              ", features=" + features +
              '}';
   }

}