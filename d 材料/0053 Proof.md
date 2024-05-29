
求解 CES 型生产函数对应的生产函数。成本最小化问题
$$\begin{aligned}
\min \ \ \ \ & \ r_1\,z_1+r_2\,z_2\\
\\
\mathrm{s.t.} \ \ \ \ & \left(z_1^{\rho}+z^\rho_2\right)^{\frac{1}\rho}=q
\end{aligned}$$

构建拉格朗日函数
$$L\left(z_1,z_2,\lambda\right)=r_1\,z_1+r_2\,z_2+\lambda\left[q-\left(z_1^{\rho}+z^\rho_2\right)^{\frac{1}\rho}\right]$$
求偏导数得一阶条件，我们的目标是从中得到最优要素投入组合
$$
\begin{cases}
\dfrac{\partial L}{\partial z_1}=r_1-\dfrac{\lambda}{\rho}\,\left( z_{1}^{\rho}+z_{2}^{\rho} \right) ^{\frac{1-\rho}{\rho}}\left( \rho \,z_{1}^{\rho -1} \right) =0&&&&(1)\\
\\
\dfrac{\partial L}{\partial z_2}=r_2-\dfrac{\lambda}{\rho}\,\left( z_{1}^{\rho}+z_{2}^{\rho} \right) ^{\frac{1-\rho}{\rho}}\left( \rho \,z_{2}^{\rho -1} \right) =0&&&&(2)\\
 \\
\dfrac{\partial L}{\partial \lambda}=q-\left(z^\rho_1+z^\rho_2\right)^{\frac1{\rho}}=0&&&&(3)
\end{cases}
$$
从 (1) 和 (2) 得
$$
\begin{aligned}
& r_1=\dfrac{\lambda}{\rho}\,\left( z_{1}^{\rho}+z_{2}^{\rho} \right) ^{\frac{1-\rho}{\rho}}\left( \rho\,z_{1}^{\rho -1} \right) \\
\\
& r_2=\dfrac{\lambda}{\rho}\,\left( z_{1}^{\rho}+z_{2}^{\rho} \right) ^{\frac{1-\rho}{\rho}}\left( \rho\,z_{2}^{\rho -1} \right) \\
\\
\Rightarrow \ \ & \dfrac{r_1}{r_2}=\dfrac{z_{1}^{\rho -1}}{z_{2}^{\rho -1}}\Rightarrow \dfrac{z_{1}^{\rho}}{z_{2}^{\rho}}=\dfrac{r_{1}^{\frac{\rho}{\rho -1}}}{r_{2}^{\frac{\rho}{\rho -1}}}&&&&(4)
\end{aligned}
$$
对生产函数进行一定的化简
$$
\begin{aligned}
{\left( z_{1}^{\rho}+z_{2}^{\rho} \right) ^{1/\rho}}&= {z_2\cdot\left( \dfrac{z_{1}^{\rho}}{z_{2}^{\rho}}+1 \right) ^{\frac{1}{\rho}}}={z_2\left( \dfrac{r_{1}^{\frac{\rho}{\rho -1}}}{r_{2}^{\frac{\rho}{\rho -1}}}+1 \right) ^{\frac{1}{\rho}}}\\
\\
&= {z_2\cdot\left( \dfrac{r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}}}{r_{2}^{\frac{\rho}{\rho -1}}} \right) ^{\frac{1}{\rho}}}={z_2\cdot\dfrac{\left( r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}} \right) ^{\frac{1}{\rho}}}{r_{2}^{\frac{1}{\rho -1}}}}\\
\end{aligned}
$$
根据等产量线约束，上式的值为 $q$，所以
$$z_2=q\cdot r_{2}^{\frac{1}{\rho -1}}\cdot \left( r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}} \right) ^{\frac{1}{\rho}}$$
同理得 
$$z_1=q\cdot r_{1}^{\frac{1}{\rho -1}}\cdot \left( r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}} \right) ^{\frac{1}{\rho}}$$

成本函数 $C\left(r_1,r_2,q\right)$ 与要素投入量无关，现在的目标是消去成本函数中的 $z_1$ 和 $z_2$
$$
\begin{aligned}
\dfrac{r_1\,z_1+r_2\,z_2}{q}&= r_{1}^{\frac{1}{\rho -1}+1}\cdot \left( r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}} \right) ^{\frac{1}{\rho}}+r_{2}^{\frac{1}{\rho -1}+1}\cdot \left( r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}} \right) ^{\frac{1}{\rho}}\\
\\
&= \left( r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}} \right) \cdot \left( r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}} \right) ^{\frac{1}{\rho}}\\
\\
&= \left( r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}} \right) ^{\frac{1+\rho}{\rho}}
\end{aligned}
$$
最终得到成本函数
$$C\left(r_1,r_2,q\right)=q\cdot\left( r_{1}^{\frac{\rho}{\rho -1}}+r_{2}^{\frac{\rho}{\rho -1}} \right) ^{\frac{1+\rho}{\rho}}$$
