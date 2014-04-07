
package math.random() {
    // defined at defs\math\random.sc: 3.1
    /** Beta distribution
     *
     * Conditions on the parameters are |alpha| > 0 and |beta| > 0.
     * Returned values range between 0 and 1.
     */
    @python.random()
    def betavariate(Alpha = 1.0,
                    Beta = 1.0) : () => Float
    
    // defined at defs\math\random.sc: 11.1
    /** Exponential distribution
     *
     *  Returned values range from 0 to positive infinity
     */
    @python.random()
    def expovariate(/** |lambda| is 1.0 divided by the desired mean. It should be greater zero.*/ Lambda = 1.0) : () => Float
    
    // defined at defs\math\random.sc: 18.1
    /** Uniform distribution
     *
     * Return a random floating point number *N* such that
     * *a* <= *N* <= *b* for *a* <= *b* and *b* <= *N* <= *a* for *b* < *a*.
     * The end-point value *b* may or may not be included in the range depending on
     * floating-point rounding in the equation *a* + (*b*-*a*) * *random()*.
     */
    @python.random()
    def uniform(Low = -10.0,
                High = 10.0) : () => Float
    
    // defined at defs\math\random.sc: 28.1
    /** Triangular distribution
     *
     * Return a random floating point number *N* such that *low* <= *N* <= *high* and
     *       with the specified *mode* between those bounds.
     *       The *low* and *high* bounds default to zero and one.
     *       The *mode* argument defaults to the midpoint between the bounds,
     *       giving a symmetric distribution.
     */
    @python.random()
    def triangular(Low = 0.0,
                   High = 1.0,
                   Mode = 0.5) : () => Float
    
    // defined at defs\math\random.sc: 39.1
    /** Gamma distribution
     *
     *  Conditions on the parameters are |alpha| > 0 and |beta| > 0.
     *
     *  The probability distribution function is: ::
     *
     *               x ** (alpha - 1) * math.exp(-x / beta)
     *     pdf(x) =  --------------------------------------
     *                  math.gamma(alpha) * beta ** alpha
     */
    @python.random()
    def gammavariate(Alpha = 1.0,
                     Beta = 1.0) : () => Float
    
    // defined at defs\math\random.sc: 52.1
    /** Log normal distribution
     *
     * If you take the natural logarithm of this distribution,
     *  you'll get a normal distribution with mean |mu| and standard deviation |sigma|.
     *  |mu| can have any value, and |sigma| must be greater than zero.
     */
    @python.random()
    def lognormvariate(Mu = 0.0,
                       Sigma = 1.0) : () => Float
    
    // defined at defs\math\random.sc: 61.1
    /** Normal distribution
     */
    @python.random()
    def normalvariate(/** |mu| is the mean                  */ Mu = 0.0,
                      /** |sigma| is the standard deviation */ Sigma = 1.0) : () => Float
    
    // defined at defs\math\random.sc: 67.1
    /** Von Mises distribution
     */
    @python.random()
    def vonmisesvariate(/** |mu| is the mean angle, expressed in radians between 0 and 2|pi|*/ Mu = 0.0,
                        /** |kappa| is the concentration parameter, which must be greater than or equal to zero.
                          *      If |kappa| is equal to zero, this distribution reduces
                          *      to a uniform random angle over the range 0 to 2|pi|        */ Kappa = 0.0) : () => Float
    
    // defined at defs\math\random.sc: 75.1
    /** Pareto distribution
     */
    @python.random()
    def paretovariate(/** |alpha| is the shape parameter*/ Alpha = 1.0) : () => Float
    
    // defined at defs\math\random.sc: 80.1
    /** Weibull distribution
     */
    @python.random()
    def weibullvariate(/** |alpha| is the scale parameter */ Alpha = 1.0,
                       /** |beta| is the shape parameter  */ Beta = 1.0) : () => Float
}
