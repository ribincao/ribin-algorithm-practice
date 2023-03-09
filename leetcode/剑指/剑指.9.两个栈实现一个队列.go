type CQueue struct {
    s1 []int;
    s2 []int;
}


func Constructor() CQueue {
    var queue CQueue;
    return queue;
}


func (this *CQueue) AppendTail(value int)  {
    this.s1 = append(this.s1, value);
}


func (this *CQueue) DeleteHead() int {
    if(len(this.s2) == 0) {
        for {
            var l1 = len(this.s1);
            if(l1 == 0) {
                break;
            }

            this.s2 = append(this.s2, this.s1[l1 - 1]);
            this.s1 = this.s1[:l1 - 1];
        }
    }
    var l2 = len(this.s2)
    if(l2 == 0) {
        return -1
    } else {
        var ret int = this.s2[l2 - 1];
        this.s2 = this.s2[:l2-1];
        return ret;
    }
}


/**
 * Your CQueue object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AppendTail(value);
 * param_2 := obj.DeleteHead();
 */