
class ImageModel {
  int id;
  String url;
  String title;

  ImageModel(this.id, this.url, this.title);

                      //keys of Strings with unk types
  ImageModel.fromJson(Map<String, dynamic> parsedJson) {
    id = parsedJson['id'];
    url = parsedJson['url'];
    title = parsedJson['title'];
  }

  //alternate syntax
  ImageModel.fromJson_2(Map<String, dynamic> parsedJson):
    id = parsedJson['id'],
    url = parsedJson['url'],
    title = parsedJson['title'];
}