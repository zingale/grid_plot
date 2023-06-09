# grid_plot is a collection of classes for defining and drawing
# finite-volume and finite-difference grids in 1- and 2-d.

import math
import sys

import matplotlib.pyplot as plt
import numpy as np


class Grid2d:
    """ the base 2-d grid """

    def __init__(self, nx, ny, ng = 0,
                 xmin=0.0, xmax=1.0, ymin=0.0, ymax=1.0):

        # finite-volume or cell-centered finite-difference
        self.nx = nx
        self.ny = ny
        self.ng = ng
        self.xmin = xmin
        self.xmax = xmax
        self.ymin = ymin
        self.ymax = ymax

        self.ilo = ng
        self.ihi = ng+nx-1
        self.jlo = ng
        self.jhi = ng+ny-1


        self.dx = (xmax - xmin)/float(nx)

        self.xl = (np.arange(2*ng+nx)-ng)*self.dx + xmin
        self.xr = (np.arange(2*ng+nx)+1-ng)*self.dx + xmin
        self.xc = 0.5*(self.xl + self.xr)

        self.dy = (ymax - ymin)/float(ny)

        self.yl = (np.arange(2*ng+ny)-ng)*self.dy + ymin
        self.yr = (np.arange(2*ng+ny)+1-ng)*self.dy + ymin
        self.yc = 0.5*(self.yl + self.yr)

    def draw_grid(self, color="k"):
        # x lines
        for n in range(self.ny):
            plt.plot([self.xmin-0.25*self.dx, self.xmax+0.25*self.dx],
                     [self.yl[self.ng+n], self.yl[self.ng+n]],
                     color=color, lw=2)

        plt.plot([self.xmin-0.25*self.dx, self.xmax+0.25*self.dx],
                 [self.yr[self.ng+self.ny-1], self.yr[self.ng+self.ny-1]],
                 color=color, lw=2)

        # y lines
        for n in range(self.nx):
            plt.plot([self.xl[self.ng+n], self.xl[self.ng+n]],
                     [self.ymin-0.25*self.dy, self.ymax+0.25*self.dy],
                     color=color, lw=2)

        plt.plot([self.xr[self.ng+self.nx-1], self.xr[self.ng+self.nx-1]],
                 [self.ymin-0.25*self.dy, self.ymax+0.25*self.dy],
                 color=color, lw=2)


    def label_center_x(self, idx, string):
        plt.text(self.xc[idx], self.yl[0]-0.35*self.dy, string,
                   horizontalalignment='center', fontsize="medium")

    def label_center_y(self, jdx, string):
        plt.text(self.xl[0]-0.35*self.dx, self.yc[jdx], string,
                   verticalalignment='center', fontsize="medium")

    def clean_axes(self):
        plt.xlim(self.xmin-0.5*self.dx, self.xmax+0.5*self.dx)
        plt.ylim(self.ymin-0.5*self.dy, self.ymax+0.5*self.dy)
        plt.axis("off")


class FVGrid2d(Grid2d):
    """ a 2-d finite-volume grid """

    def label_cell_center(self, idx, jdx, string, fontsize="medium", color="k"):
        plt.text(self.xc[idx], self.yc[jdx],
                 string, fontsize=fontsize, color=color,
                 horizontalalignment='center', verticalalignment='center')

    def shade_cell(self, idx, jdx):
        xl = self.xl[idx]
        xr = self.xr[idx]
        yl = self.yl[jdx]
        yr = self.yr[jdx]
        plt.fill([xl, xl, xr, xr, xl], [yl, yr, yr, yl, yl], "0.75")

    def mark_cell_left_state_x(self, idx, jdx, string, color="k",
                               fontsize="medium"):
        plt.scatter(self.xr[idx]-0.05*self.dx, self.yc[jdx],
                      marker="x", s=50, color=color)
        plt.text(self.xr[idx]-0.075*self.dx, self.yc[jdx], string,
                   fontsize=fontsize, rotation="270", color=color,
                   horizontalalignment='right', verticalalignment='center')

    def mark_cell_right_state_x(self, idx, jdx, string, color="k",
                                fontsize="medium"):
        plt.scatter(self.xl[idx]+0.05*self.dx, self.yc[jdx],
                      marker="x", s=50, color=color)
        plt.text(self.xl[idx]+0.075*self.dx, self.yc[jdx], string,
                   fontsize=fontsize, rotation="270", color=color,
                   horizontalalignment='left', verticalalignment='center')

    def mark_cell_state_y(self, idx, jdx, string, color="k",
                          fontsize="medium", off_sign=1.0):
        plt.scatter(self.xc[idx], self.yr[jdx],
                      marker="x", s=50, color=color)
        if off_sign > 0:
            align = "bottom"
        else:
            align = "top"

        plt.text(self.xc[idx], self.yr[jdx]+off_sign*0.05*self.dy, string,
                   fontsize=fontsize, rotation="0", color=color,
                   horizontalalignment='center', verticalalignment=align)

    def mark_cell_left_state_y(self, idx, jdx, string, color="k",
                               fontsize="medium"):
        plt.scatter(self.xc[idx], self.yr[jdx]-0.05*self.dy,
                      marker="x", s=50, color=color)
        plt.text(self.xc[idx], self.yr[jdx]-0.075*self.dy, string,
                   fontsize=fontsize, rotation="0", color=color,
                   horizontalalignment='center', verticalalignment='top')

    def mark_cell_right_state_y(self, idx, jdx, string, color="k",
                                fontsize="medium"):
        plt.scatter(self.xc[idx], self.yl[jdx]+0.05*self.dy,
                      marker="x", s=50, color=color)
        plt.text(self.xc[idx], self.yl[jdx]+0.075*self.dy, string,
                   fontsize=fontsize, rotation="0", color=color,
                   horizontalalignment='center', verticalalignment='bottom')



class FDGrid2d(Grid2d):
    """ a 2-d finite-difference grid """

    def label_cell_center(self, idx, jdx, string, fontsize="medium", color="k"):
        plt.scatter([self.xc[idx]], [self.yc[jdx]], marker="x", color=color)
        plt.text(self.xc[idx]+0.075*self.dx, self.yc[jdx]+0.075*self.dy,
                 string, fontsize=fontsize, color=color,
                 horizontalalignment='left', verticalalignment='center')
