func reverseString(s []byte)  {
    i, j := 0, len(s) - 1;
    for {
        if i >= j {
            break;
        }
        tmp := s[i];
        s[i] = s[j];
        s[j] = tmp;

        i += 1;
        j -= 1;
    }
}