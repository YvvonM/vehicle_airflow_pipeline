{{ config(
    materialized = 'view'
) }}

with vehicle_identity as (
    select * from public.tracks
),


vehicle_trajectory as(
    select * from public.trajectory
)

select * from vehicle_trajectory