{{config(
    materialized = 'view'
)}}

WITH highest_dist_covered AS (
    SELECT
        track_id,
        type,
        traveled_d
    FROM
        public.tracks
    ORDER BY
        traveled_d DESC
)

SELECT * FROM highest_dist_covered
