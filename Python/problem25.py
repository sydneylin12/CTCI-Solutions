# Regex tester for . and *

def regex(exp, s):
    i = 0 # expression index
    j = 0 # string index

    # Iterate through both with pointers to different idices
    while i < len(exp) and j < len(s):  
        print("(" + exp[i] + " , " + s[j] + ")")

        # Check for periods - one character swap
        if exp[i] == ".":
            # Move index up for both strings
            i += 1
            j += 1

        # Assume star has to have a character before
        # Do not assume star has a character after
        # Star only matches one previous element
        elif exp[i] == "*":
            query = exp[i-1]
            print("Star found with query: " + query + " at index: " + str(i))

            # Return true if star is end of string
            if i + 1 >= len(exp) and query == ".":
                print("End of string case with .*")
                return True

            # Must match previous character
            else:
                next = exp[i + 1]
                print("Next character as breaking character: " + next)

                # Dot star = all characters any amount of times
                if query == ".":
                    while s[j] != next:
                        j += 1
                # Only previous character any amount of times
                else:
                    while s[j] == query:
                        j += 1

            # Advance the expression index when done
            i += 1

        # Check for same character
        elif exp[i] == s[j]:
            print("Characters equal: " + str(exp[i]))
            i += 1
            j += 1

        # Non equal characters - already checked for * and .
        elif exp[i] != s[j]:
            print("Non matching characters detected: " + exp[i] + " & " + s[j])
            return False
    
        # Just in case
        else:
            return False

    # When you reach the end of the string

    print("(" + str(i) + " , " + str(j) + ")")
    if i == len(exp) and j == len(s):
        return True
        
    return False


print(regex("ra.*az*a", "rayquazzzzzza"))