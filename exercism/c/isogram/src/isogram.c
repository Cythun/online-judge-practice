#include "isogram.h"

bool is_isogram(const char phrase[])
{
    int len;
    int alphabet[26] = {0};
    int temp;
    
    if (!phrase)
    {
        return false;
    }

    len = strlen(phrase);

    for (int i = 0; i < len; i++)
    {
        if (isalpha(phrase[i])) 
        {
            temp = tolower(phrase[i]);
            temp = temp - 97;
            if (alphabet[temp] > 0)
            {
                return false;
            }
            else
            {
                alphabet[temp] = 1;
            }
        }
    }
    return true;
}