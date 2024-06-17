
  
    

  create  table "Data-warehouse"."public"."my_model__dbt_tmp"
  
  
    as
  
  (
    -- with doctorset as (
--     select * from "Data-warehouse"."public"."doctorset_raw"
-- ),
-- eahci as (
--     select * from "Data-warehouse"."public"."eahci_raw"
-- ),
-- yetenaweg as (
--     select * from "Data-warehouse"."public"."yetenaweg_raw"
-- ),
-- lobelia4cosmetics as (
--     select * from "Data-warehouse"."public"."lobelia4_raw"
-- )

-- select
--     doctorset.id,
--     doctorset.image_id,
--     doctorset.x_min,
--     doctorset.y_min,
--     doctorset.x_max,
--     doctorset.y_max,
--     doctorset.confidence,
--     doctorset.class_id,
--     doctorset.class_name,
--     doctorset.timestamp
-- from doctorset

-- union all

-- select
--     eahci.id,
--     eahci.image_id,
--     eahci.x_min,
--     eahci.y_min,
--     eahci.x_max,
--     eahci.y_max,
--     eahci.confidence,
--     eahci.class_id,
--     eahci.class_name,
--     eahci.timestamp
-- from eahci

-- union all

-- select
--     yetenaweg.id,
--     yetenaweg.image_id,
--     yetenaweg.x_min,
--     yetenaweg.y_min,
--     yetenaweg.x_max,
--     yetenaweg.y_max,
--     yetenaweg.confidence,
--     yetenaweg.class_id,
--     yetenaweg.class_name,
--     yetenaweg.timestamp
-- from yetenaweg

-- union all

-- select
--     lobelia4cosmetics.id,
--     lobelia4cosmetics.image_id,
--     lobelia4cosmetics.x_min,
--     lobelia4cosmetics.y_min,
--     lobelia4cosmetics.x_max,
--     lobelia4cosmetics.y_max,
--     lobelia4cosmetics.confidence,
--     lobelia4cosmetics.class_id,
--     lobelia4cosmetics.class_name,
--     lobelia4cosmetics.timestamp
-- from lobelia4cosmetics






with doctorset as (
    select * from "Data-warehouse"."public"."doctorset_raw"
),
eahci as (
    select * from "Data-warehouse"."public"."eahci_raw"
),
yetenaweg as (
    select * from "Data-warehouse"."public"."yetenaweg_raw"
),
lobelia4cosmetics as (
    select * from "Data-warehouse"."public"."lobelia4_raw"
)

select
    doctorset.id,
    doctorset.image_id,
    doctorset.x_min,
    doctorset.y_min,
    doctorset.x_max,
    doctorset.y_max,
    doctorset.confidence,
    doctorset.class_id,
    doctorset.class_name,
    doctorset.timestamp
from doctorset

union all

select
    eahci.id,
    eahci.image_id,
    eahci.x_min,
    eahci.y_min,
    eahci.x_max,
    eahci.y_max,
    eahci.confidence,
    eahci.class_id,
    eahci.class_name,
    eahci.timestamp
from eahci

union all

select
    yetenaweg.id,
    yetenaweg.image_id,
    yetenaweg.x_min,
    yetenaweg.y_min,
    yetenaweg.x_max,
    yetenaweg.y_max,
    yetenaweg.confidence,
    yetenaweg.class_id,
    yetenaweg.class_name,
    yetenaweg.timestamp
from yetenaweg

union all

select
    lobelia4cosmetics.id,
    lobelia4cosmetics.image_id,
    lobelia4cosmetics.x_min,
    lobelia4cosmetics.y_min,
    lobelia4cosmetics.x_max,
    lobelia4cosmetics.y_max,
    lobelia4cosmetics.confidence,
    lobelia4cosmetics.class_id,
    lobelia4cosmetics.class_name,
    lobelia4cosmetics.timestamp
from lobelia4cosmetics
  );
  