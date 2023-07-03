import cpp

 

class NetworkByteSwap extends Expr {
  NetworkByteSwap () {
    exists(MacroInvocation mi, Macro m |
        this = mi.getExpr() and
        mi.getMacro() = m and
        (m.getName() = "ntohs" or
        m.getName() = "ntohl" or
        m.getName() = "ntohll")
    )
  }
}

 

from NetworkByteSwap n
select n, "Network byte swap"