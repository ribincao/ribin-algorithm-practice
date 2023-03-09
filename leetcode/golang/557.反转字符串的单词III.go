import "strings"
func reverseWords(s string) string {
    ss := strings.Split(s, string(' '));
    var ret []string;
    for _, chs := range ss {
        tmp := reverse([]rune(chs));
        ret = append(ret, string(tmp));
    }
    return strings.Join(ret, string(' '));
};

func reverse(s []rune) []rune {
    var ret []rune;
    i := len(s) - 1;
    for {
        if i < 0 {
            break;
        }
        ret = append(ret, s[i]);
        i -= 1;
    }
    return ret;
}