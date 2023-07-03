import cpp
import semmle.code.cpp.dataflow.TaintTracking
import DataFlow::PathGraph

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

class Config extends TaintTracking::Configuration {
  Config() { this = "NetworkToMemFuncLength" }

  override predicate isSource(DataFlow::Node source) {
    source.asExpr() instanceof NetworkByteSwap
  }

  override predicate isSink(DataFlow::Node sink) {
    // sink should be the size argument of calls to memcpy
    (exists(FunctionCall call | sink.asExpr() = call.getArgument(2) and
    call.getTarget().getName() = "memcpy"))
  }
}

from Config cfg, DataFlow::PathNode source, DataFlow::PathNode sink
where cfg.hasFlowPath(source, sink)
select sink, source, sink, "Lo scambio di byte di rete passa a memcpy"