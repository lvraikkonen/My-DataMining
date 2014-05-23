# import data
x <- read.csv("country_data.csv", header=TRUE, row.names=1)

# run K-Means (3groups)
km <- kmeans(x, 3, 15)

# print components of km
print(km)

# plot clusters
plot(x, col = km$cluster)
# plot centers
points(km$centers, col = 1:2, pch = 8)
