"""!

@file geometry.py
@brief Fichier qui contient diverse fonction de calcul d'air et de périmètre

"""

def rectangle_area(lenght, width):
	"""!
	Retourne l'air d'un rectangle

	@param lenght Longueur du rectangle
	@param width Largeur du rectangle
	"""

	return lenght * width

def rectangle_perimeter(lenght, width):
        """!
        Retourne le perimetre d'un rectangle

        @param lenght Longueur du rectangle
        @param width Largeur du rectangle
        """

        return ((lenght * 2) + (width * 2))

def circle_area(radius):
        """!
        Retourne l'air d'un cercle

        @param radius rayon du cercle
        """

        return 3.14 * (radius * radius)


def circle_circumference(radius):
        """!
        Retourne la circonference d'un cercle

        @param radius rayon du cercle
        """

        return 3.14 * (2 * radius)
