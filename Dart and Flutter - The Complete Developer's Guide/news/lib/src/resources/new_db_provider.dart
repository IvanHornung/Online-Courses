import 'package:sqflite/sqflite.dart';
import 'package:path_provider/path_provider.dart';
import 'dart:io';
import 'package:path/path.dart';
import 'dart:async';
import '../models/item_model.dart';

class NewsDbProvider {
  Database db;

  //cannot assign async to a Constructor, so...
  //init tries to create a database or attempt to reopen it
  init() async {
    //for mobile devices, returns reference to a little folder where we can safely store some data
    Directory documentsDirectory = await getApplicationDocumentsDirectory();
    //documentsDirectory is a folder reference. $.path speaks for itself.
    final path = join(documentsDirectory.path,
        "items.db"); //join the path + the word "items.db" together
    db = await openDatabase(
      path, //create if not exist, or just use path
      version: 1, //internal record for me
      onCreate: (Database newDb, int version) {
        //only called the very first time our user starts our applications
        newDb.execute("""
          CREATE TABLE Items
          (
            id INTEGER PRIMARY KEY,
            type TEXT,
            by TEXT,
            time INTEGER,
            text TEXT,
            parent INTEGER,
            kids BLOB,
            dead INTEGER,
            deleted INTEGER,
            url TEXT,
            score INTEGER,
            title TEXT,
            descendants INTEGER
          )
        """);
      },
    );
  }

  fetchItem(int id) async {
    final maps = await db.query(
      "Items",
      columns: null, //we want the entire item
      where: "id = ?", //prevents sqlite injection hack
      whereArgs: [id], //parameter to func
    );

    if (maps.length > 0) {
      return ItemModel.fromDb(maps.first); //first map from maps
    }
    return null;
  }

  addItem(ItemModel item) {
    return db.insert("Items", item.toMapForDb());
  }
}
