
package observable.sidefunc {
    def Noise(side_distribution = mathutils.rnd.uniform(0.0,1.0))
         = if side_distribution>0.5 then 0.0 else 1.0
}
