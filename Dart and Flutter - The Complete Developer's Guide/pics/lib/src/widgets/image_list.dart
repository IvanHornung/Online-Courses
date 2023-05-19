import 'package:flutter/material.dart';
import '../models/image_model.dart';

//because ImageList itself is not in charge of changing variables...
class ImageList extends StatelessWidget {
  final List<ImageModel> images;

  ImageList(this.images);

  Widget build(context) {
    return ListView.builder(
        itemCount: images.length,
        itemBuilder: (context, int index) {
          return buildImage(images[index]);
        });
  }

  //not special
  Widget buildImage(ImageModel image) {
    return Container(
      //Boarder
      decoration: BoxDecoration(
        border: Border.all(color: Colors.grey),
      ),
      padding: EdgeInsets.all(20.0),
      //class that defines spacing around an element
      //all(double pixels) refers to all sides of container (T,B,L,R)
      margin: EdgeInsets.all(20.0),
      //child is widget displayed inside whatever ur trying to make
      child: Column( //column widget stacks up widgets
        children: <Widget>[ //declaring a list of widgets to be safe
          Padding(
            child: Image.network(image.url),
            padding: EdgeInsets.only(
              bottom: 8.0,
            ),
          ),
          Text(image.title),
        ],
      ),
    );
  }
}

/*
           V-Border
    |Margin|Padding|Widget Body|
*/
