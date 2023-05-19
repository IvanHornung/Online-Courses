int main() {
  int x = 1;
  
  /*if-statements are practically the same as Java*/
  if(x==1)
    printf("Correct");
  else
    printf("bruh.");
    
    
  switch(x) { /*must have breaks. if case 0, continue all executions*/
    case 0:
      y = 1;
    case 1:
      y = 2;
      break;
    case 2:
      y = 3;
    
    }
}
