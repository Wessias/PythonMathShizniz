import matplotlib.pyplot as plt 
import scipy.interpolate as ap 
import numpy as np 
import matplotlib.animation as animation


def animate(points, result, filename, aniSeconds= 5, fps = 30):
    
    
    # Get the ts analyzed in the method
    ts = result.t 
    tstart = ts[0]+1e-8
    tend  = ts[-1]-1e-8
    
    # Get the y(t) for each t analyzed
    ys = result.y 
    px, py = ys[0,:],ys[1,:] 
    # Interpolate with splines
    cpx = ap.interp1d(ts,px, kind = 'cubic')
    cpy = ap.interp1d(ts,py,kind = 'cubic') 
    
    # Plotting things
    fig,ax = plt.subplots()
    ln, = plt.plot([],[],'r.')
    
    #First plott all the static points
    def init():
        for point in points: #Go through points
            ax.plot(point[0],point[1],'b.') #Plot each point
        return ln,

    #Generate fps*aniSeconds number of timesteps in the time frame
    dts=np.linspace(tstart,tend,fps*aniSeconds)
    #Add extra half second where nothing happens at the end 
    dts = np.hstack((dts,tend*np.ones(int(fps*0.5))))
    
    def update(i):
        xdata = [float(cpx(dts[i]))]
        ydata = [float(cpy(dts[i]))]
        ln.set_data(xdata, ydata)
        return ln,
    
    ani = animation.FuncAnimation(fig, update, frames=len(dts),
                                  interval = int(1000/fps),
                                  init_func=init, blit=True)
    
    ani.save(filename,writer = animation.PillowWriter(fps=fps))
    
