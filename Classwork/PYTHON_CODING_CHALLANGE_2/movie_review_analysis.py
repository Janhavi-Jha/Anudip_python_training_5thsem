'''Ratings given by users for movies are stored below.
Sample Data
ratings = {
 "Inception": 4.8,
 "Avatar": 4.3,
 "Titanic": 4.5,
 "Joker": 4.7,
 "Frozen": 3.8,
 "Interstellar": 4.9,
 "Dune": 4.6,
 "Up": 4.1,
 "Coco": 4.4,
 "Cars": 3.9
}
Tasks
1. Display movies rated above 4.5.
2. Find the highest-rated movie.
3. Find the lowest-rated movie.
4. Calculate average rating.
5. Create a recommendation list (rating ≥ 4.5). '''
ratings = {
 "Inception": 4.8,
 "Avatar": 4.3,
 "Titanic": 4.5,
 "Joker": 4.7,
 "Frozen": 3.8,
 "Interstellar": 4.9,
 "Dune": 4.6,
 "Up": 4.1,
 "Coco": 4.4,
 "Cars": 3.9
}
#display movie rated above 4.5
print("Movie with ratings above 4.5=")
for i in ratings.items():
    if i[1]>4.5:
        print(i[0])
#highest rated movie
highest=0
movie=" "
for i in ratings.items():
    if i[1]>highest:
        highest=i[1]
        movie=i[0]
print("The highest rated movie is ",movie)
#lowest rated movie
lowest=4.8
movies=" "
for i in ratings.items():
    if i[1]<lowest:
        lowest=i[1]
        movies=i[0]
print("The lowest rated movie is ",movies)
#average rating
total=0
for i in ratings.items():
    total+=i[1]
average=total/len(ratings)
print("Average=",average)
#recommended list
recommend=[]
for i in ratings.items():
    if i[1]>=4.5:
        recommend.append(i[0])
print("Recommended movies=",recommend)