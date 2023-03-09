func convertToTitle(columnNumber int) string {
    ret := make([]rune, 0);
    for {
        if columnNumber == 0 {
            break;
        }
        c := columnNumber % 26;
        columnNumber = columnNumber / 26;
        if c == 0 {
            ret = append(ret, 'Z');
            columnNumber -= 1;
        } else {
            ch := rune(c - 1 + int('A'));
            ret = append(ret, ch);
        }
    }

    //  逆序
    i, j := 0, len(ret) - 1;
    for {
        if i >= j {
            break;
        }
        tmp := ret[i];
        ret[i] = ret[j];
        ret[j] = tmp;

        i += 1;
        j -= 1;
    }

    return string(ret);
}