import pandas as pd
data={"Movie":["LEO","VIKRAM","JAILER","96","SITA RAMAM","MASTER","KAITHI","LOVE TODAY","RATHASAN","ANBE SIVAM","BIGIL","YOUTH","PETROMAX","DHURANDHAR","OK OK","KANCHANA","CONJURING","ANNABELLE","THE NUN","IT"],
               "Genre":["ACTION","ACTION","ACTION","ROMANCE","SENTIMENT","FANTASY","SENTIMENT","ROMANCE","THRILLER","FANTASY","SENTIMENT","COMEDY","COMEDY","THRILLER","COMEDY","HORROR","HORROR","HORROR","HORROR","HORROR"]}
df = pd.DataFrame(data)
moviename=input("ENTER THE FAVOURITE MOVIE:")
genre=df[df["Movie"] == moviename]["Genre"].values[0]
recommendations=df[df["Genre"] == genre]
recommendations=recommendations[recommendations["Movie"] != moviename]
print(recommendations)
