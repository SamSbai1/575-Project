library(PhysicalActivity)

dat <- readActigraph('D:/WSU/CptS 475 (Data Science)/Project/Git repo/575-Project/Participant2/AccelrometerData.agd', convertTime = TRUE)
write.csv(dat, 'D:/WSU/CptS 475 (Data Science)/Project/Git repo/575-Project/Participant2/AccelrometerData.csv', row.names = FALSE)
