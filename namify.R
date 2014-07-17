library(ggplot2)

words <- read.table("namics.txt")
occurrences <- as.data.frame(table(words$V1))

ggplot(occurrences, aes(x=reorder(Var1, Freq), y=Freq)) + 
  xlab("word") + ylab("occurrence") +
  geom_point() + theme(axis.text.x = element_text(angle=90, hjust=TRUE))