ptrs=0x56559094
p=0xffffcf6c
pat_on_back=0x56556241

d_ptrs_p= p-ptrs
d_ptrs_pat= p- pat_on_back

fx = open("log.txt","w")
print("Ptrs: " , ptrs ,"\nP: ", p , "pat: " , pat_on_back , "\n\nHEX\nPtrs: ", hex(ptrs) ,"\nP: ", hex(p) , "\npat: " , hex(pat_on_back), "\n\nDISTANZA ptrs-p: ",d_ptrs_p ,"\nDISTANZA ptrs-pat: ",d_ptrs_pat , "\n\nHEX DISTANZA ptrs-p: ",hex(d_ptrs_p) ,"\nDISTANZA ptrs-pat: ",hex(d_ptrs_p),"\n\n DIV4 DISTANZA ptrs-p: ",d_ptrs_p/4 ,"\nDISTANZA ptrs-pat: ",d_ptrs_pat/4 ,file=fx)
fx.close()