def main():
    top_artists = ["The Beatles", "Madonna", "Elton John", "Elvis Presley", "Mariah Carey", "Stevie Wonder", "Janet Jackson", "Michael Jackson", "Whitney Houston", "Rihanna"]
    def artist_replace():
        try:
            artist_index = int(input("Enter the index of the artist you currently want to replace:  "))
            assert -len(top_artists) <= artist_index < len(top_artists), "The number does not fall within range of list, IndexError"

            artist_new = input("Enter the name of the artist you want to add")
            top_artists[artist_index] = artist_new
            print("Artist has been added")
            print(top_artists)

        except ValueError:
            raise ValueError("Invalid input for artist index")
        except TypeError:
            raise TypeError("The integer for artists index is invalid")
        except Exception as e:
            print("A new error has been found:", e)



    artist_replace()

main()
