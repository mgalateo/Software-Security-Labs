import cpp

from  Macro m , MacroInvocation mi
where
    mi.getMacro() =m and
    (m.getName()="ntohs" or m.getName()="ntohl" or m.getName()="ntohll")
select mi.getExpr()