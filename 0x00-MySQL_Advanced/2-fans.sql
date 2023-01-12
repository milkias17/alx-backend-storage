-- rank country origins of bands, ordered by the number of (non-unique) fans.
SELECT
  origin,
  SUM(fans) AS nb_fans
from
  metal_bands
GROUP BY
  origin
ORDER BY
  SUM(fans) DESC;
