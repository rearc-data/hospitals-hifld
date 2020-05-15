<a href="https://www.rearc.io/data/">
    <img src="./rearc_logo_rgb.png" alt="Rearc Logo" title="Rearc Logo" height="52" />
</a>

# Hospitals Dataset | Homeland Infrastructure Foundation-Level Data (HIFLD)

You can subscribe to the AWS Data Exchange product utilizing the automation featured in this repository by visiting [https://aws.amazon.com/marketplace/pp/prodview-pg52qkffii33s](https://aws.amazon.com/marketplace/pp/prodview-pg52qkffii33s). 

## Main Overview
This dataset contains locations and resources of Hospitals for 50 US states, Washington D.C., US territories of Puerto Rico, Guam, American Samoa, Northern Mariana Islands, Palau, and Virgin Islands.

The dataset only includes hospital facilities based on data acquired from various state departments or federal sources which has been referenced in the SOURCE field. Hospital facilities which do not occur in these sources will be not present in the database. The source data was available in a variety of formats (pdfs, tables, webpages, etc.) which was cleaned and geocoded and then converted into a spatial database. The database does not contain nursing homes or health centers. Hospitals have been categorized into children, chronic disease, critical access, general acute care, long term care, military, psychiatric, rehabilitation, special, and women based on the range of the available values from the various sources after removing similarities.

### Data Sources
The included dataset features the following columns:

`X, Y, OBJECTID, ID, NAME, ADDRESS, CITY, STATE, ZIP, ZIP4, TELEPHONE, TYPE, STATUS, POPULATION, COUNTY, COUNTYFIPS, COUNTRY, LATITUDE, LONGITUDE, NAICS_CODE, NAICS_DESC, SOURCE, SOURCEDATE, VAL_METHOD, VAL_DATE, WEBSITE, STATE_ID, ALT_NAME, ST_FIPS, OWNER, TTL_STAFF, BEDS, TRAUMA, HELIPAD`

## More Information
- [Source: Homeland Infrastructure Foundation-Level Data (HIFLD) Open Data](https://hifld-geoplatform.opendata.arcgis.com)  
- [HIFLD | Hospitals Dataset Homepage](https://hifld-geoplatform.opendata.arcgis.com/datasets/hospitals)
- Frequency: Weekly
- Format: GeoJSON, CSV

## Contact Details
- If you find any issues with or have enhancement ideas for this product, open up a GitHub [issue](https://github.com/rearc-data/hospitals-hifld/issues) and we will gladly take a look at it. Better yet, submit a pull request. Any contributions you make are greatly appreciated :heart:.
- If you are looking for specific open datasets currently not available on ADX, please submit a request on our project board [here](https://github.com/rearc-data/covid-datasets-aws-data-exchange/projects/1).
- If you have questions about the source data, please contact HIFLD@hq.dhs.gov.
- If you have any other questions or feedback, send us an email at data@rearc.io.

## About Rearc
Rearc is a cloud, software and services company. We believe that empowering engineers drives innovation. Cloud-native architectures, modern software and data practices, and the ability to safely experiment can enable engineers to realize their full potential. We have partnered with several enterprises and startups to help them achieve agility. Our approach is simple — empower engineers with the best tools possible to make an impact within their industry.
