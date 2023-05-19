'''    belongs to
|Album|<------- |Track  |
                |Title  |   TRACK
                |Rating |    id   *Primary key*
                |Len    |   title *Logical key*
                |Count  |   rating
          Album              len
            id<----|         count
           title   |-------album_id *Foreign key*

create from outward in.
'''
