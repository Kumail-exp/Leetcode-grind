class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        flip=lambda x: x^1
        for i in range(len(image)):
            for j in range(len(image[i])//2 +len(image[i])%2):
                k=len(image[i])-j-1
                image[i][j],image[i][k]=flip(image[i][k]),flip(image[i][j])
        return image