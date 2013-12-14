package observable.sidefunc
{
    def Noise(side_distribution = mathutils.rnd.uniform(0., 1.)) =
        if side_distribution > 0.5 then 0 else 1
}