/*--Plan of Attack--
-User starts app up
- We want ot show list of 'top stories'
- Make request to get ID's of top stories
- For each ID, make additional requestto get details
- User taps on a story
- Get each 'kid' id, make additional request to get comments
- For each comment fetched, look at each 'kids' list, make additional req


*If we were doing a real worl app*
                   ->
Our App -> Our API ->Hacker News api
                   ->
Our API would be responsible for all our requests
instead of the app.

-Performance Strategy-
.                                      (checks local cache to see if we have fetch this before)
Our app decides it                             --> NewsDbProvider Class -> Sqlite Database on Device
needs to fetch an Item   -> Repository class --
.                                              --> NewsApiProvider Class -> HackerNews Api
.                                                  (Fetches item from API)
*/
