

%%NOT WORKING GO TO PYTHON FOR FINAL WORKINg

I = imread("Jellyfish.jpg");
J = imread("tulip.jpg");

%II = im2gray(I);
%II = imresize(II,0.2);

JJ = im2gray(J);
%JJ = im2gray(I);

ascii = '?@$%:!+^.';

Len = length(ascii)-1;

XX = 255/Len;
XX = floor(XX);

art = {};


[L,H] = size(JJ);

for y = 1:H-1
    line={};
    
    for x = 1:L-1
            intensity_value = JJ(y,x);
            
            index = intensity_value/XX;
            index = floor(index);
            index = int32(index);
            disp(index);
            a = ascii(index+1);
            
            line = [line, a];
            
            
    end
    line = [line, '\n'];
    
    art = [art, line];
end


fid = fopen( 'results.txt', 'wt' );
for i = 1:length(art)
      a = art(i);
    if art(i) == "\n"
        fprintf( fid, '%s\n', string(a));
    else
    fprintf( fid, '%s', string(a));
    end
  
    
end
fclose(fid);

type results.txt

