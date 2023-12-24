-- models/vehiclessql/Merged_View.sql

{{ config(
    materialized = 'view'
) }}

-- Define the Merged_View
with merged_data as (
    select
        t.type,
        t.traveled_d,
        t.avg_speed,
        tr.*  -- Select all columns from the trajectory table
    from
        public.tracks t
    join
        public.trajectory tr on t.track_id = tr.track_id
),

 average_time AS (SELECT
    track_id,
    AVG(time) AS avg_time_used
FROM
    merged_data
GROUP BY
    track_id)


select * from average_time
