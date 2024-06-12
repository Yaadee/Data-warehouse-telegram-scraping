
with source_data as (
  select
    id,
    date,
    lower(text) as text,
    sender_id,
    views
  from {{ source('my_source', 'source_table') }}
)

select
  id,
  date,
  text,
  sender_id,
  views
from source_data




