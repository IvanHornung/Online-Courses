%Write a function called blur that blurs the input image. The function is to be called like this:
%output = blur(img,w);
%where img, the input image is a two-dimensional matrix of grayscale pixel values between 0 and 255. 
% Blurring is to be carried out by averaging the pixel values in the vicinity of every pixel. Specifically,
% the output pixel value is the mean of the pixels in a square submatrix of size 2w+1 where the given pixel 
% sits in the center. For example, if w is 1, then we use a 3x3 matrix, that is, we average all the neighboring pixels
% of the given pixel and itself. Only use valid pixels when portions of the blurring matrix fall outside the image.
% For example, the blurred value corresponding to w = 1 at index (1,1) would be the mean of of elements (1,1), (1, 2),
% (2,1) and (2, 2). Both input img and output output are of type uint8.
%You can download the test image here


function [output] = blur(img, w)
    [m n] = size(img);
    img = uint8(img);
    mige = nan(size(img) + (2*w));
    mige(w + 1:end-w, w + 1:end-w) = img;
    output = 0 * img;
    for i = w + 1:m + w
      for v = w + 1:n + w
        tmp = mige(i - w:i + w,v - w:v + w);
        output(i - w,v - w) = mean(tmp(~isnan(tmp)));
      end
    end
    output = uint8(output);
