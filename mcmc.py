import numpy as np

'''
mcmc:  function to perform a simple MCMC using the Metropolis-Hastings Algorithm

Inputs:
func  - the function to be used for fitting. Function should accept 2 inputs
        the first is the x-values at which the model is calculated, the second
        is a numpy array for the parameters.
x     - the x-values at which the model should be calculated (numpy array)
y     - the value of the data for each x (numpy array)
sig   - the uncertainty on y (numpy array)
pars0 - The initial paramters from which to start the MCMC chain (numpy array)
stepsize - the stepsize for each of the parameters (numpy array)
nstep    - the number of steps in the MCMC chain

Outputs:
chain    - The MCMC chain as a (Nsteps, Npars) numpy array
'''
def mcmc(func,x,y,sig,pars0,stepsize,nstep=1e4):
    nstep=int(nstep)
    npars=pars0.shape[0]
    chain=np.zeros((int(nstep),npars))
    chi2=np.zeros(int(nstep))

    chain[0,:]=pars0.copy()
    mdl=func(x,pars0)
    chi2[0]=np.sum( (y-mdl)**2/sig**2)
    njump=0
    for i in range(1,nstep):
        pars_new=np.random.normal(chain[i-1,:],stepsize)
        mdl=func(x,pars_new)
        chi2_new=np.sum( (y-mdl)**2/sig**2)
        if (chi2_new > chi2[i-1]):
            p0=np.exp(-(chi2_new-chi2[i-1])/2.)
            p=np.random.uniform(0,1,1)
            if  p<=p0:
                chain[i,:]=pars_new
                chi2[i]=chi2_new
                njump=njump+1
            else:
                chain[i,:]=chain[i-1,:]
                chi2[i]=chi2[i-1]
        else:
            chain[i,:]=pars_new
            njump=njump+1
            chi2[i]=chi2_new
    print('Jump fraction: %.3f' %(njump/nstep))
    return chain
