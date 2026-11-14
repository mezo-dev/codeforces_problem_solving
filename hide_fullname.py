

class HideFullName:
    def hide_full_name(self, full_name: str) -> str:

        result = ""
        start = 0

        for i in range(len(full_name)): 

            if full_name[i] == " ":
                
                for j in range(start, i):
                    result += "*" if start == 0 else (
                        full_name[j]  if j == i - 1 else "*"
                    )
                
                result += " "
                start = i + 1


            for j in range(start, len(full_name)):
                result += full_name[j] if j == len(full_name) - 1 else "*"
            
            return result
        
        return result

            

obj = HideFullName()
print(obj.hide_full_name("moataz fawzy elsayed"))