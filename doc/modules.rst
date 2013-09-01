Simple modules

Normally they return None if one of the operands is None

- Constant[T]/None[T] functions
- Identity function
- Arithmetic operations (+,-,*,/,%)
- Comparisons (<, <=, >, >=, ==, !=)
- Conditional branching (condition ? trueBranch : falseBranch)
- Math module functions (Exp, Pow, Log, Atan etc.)
- Random distrubutions (uniform, lognormvariate, expovariate etc.)
- Derivative of a differentiable function

Max(x,y) ::= x > y ? x : y
Min(x,y) ::= x < y ? x : y
Sqr(x) ::= x*x


Statistics:
- average: cumulative (CMA), moving (MA), exponentially weighted (EWMA)
- variance: cumulative (Variance), moving (MovingVariance), exponentially weighted (EWMV)
- moving minimum/maximum

Variances could be implemented as Var(x) ::= Mean(Sqr(x)) - Sqr(Mean(x)) but it may loose precision

StdDev(x) ::= Sqrt(Variance(x))

Relative strength index
	UpMovements(x, dt) ::= max(0, x - Lagged(x, dt))
	DownMovements(x, dt) ::= max(0, Lagged(x, dt) - x)
	RSI(x, dt, alpha) ::= 100 - 100 / (1 + EWMA(UpMovements(x,dt), alpha)/EWMA(DownMovements(x,dt), alpha))

- Moving average convergence/divergence
	MACD(x, slow, fast) ::= EWMA(x, 2./(fast+1)) - EWMA(x, 2./(slow+1))
	MACD_signal(x, slow, fast, timeframe) ::= EWMA(MACD(x, slow, fast), 2/(timeframe+1))
	MACD_histogram(x, slow, fast, timeframe) ::= MACD(x,slow,fast) - MACD_signal(x,slow, fast, timeframe)

- Bollinger bands
	Bollinger_Hi(x) ::= Mean(x) + 2*StdDev(x)
	Bollinger_Lo(x) ::= Mean(x) - 2*StdDev(x)

- Quotes: downloading external historical data

