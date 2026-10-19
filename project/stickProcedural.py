"""
Module containing functions to edit stick figure scene with a Procedural
programming approach and a `Render` class to create an `.avi` file of
the created scene.
"""

import json
import os

import cv2
import numpy as np


def createCharacter(
    sceneName: str, charName: str, posx: int
) -> tuple[
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
    np.ndarray,
]:
    """
    A function for creating a Person Stick figure

    Parameters
    ----------
    sceneName : str
        name of scene
    charName : str
        name of character
    posx : int
        Starting x-position of Character, should be 0 ≤ posx ≤ 1920

    Returns
    -------
    np.ndarray
        right_hand 2-element positional array
    np.ndarray
        right_elbow 2-element positional array
    np.ndarray
        chest 2-element positional array
    np.ndarray
        hips 2-element positional array
    np.ndarray
        head 2-element positional array
    np.ndarray
        left_elbow 2-element positional array
    np.ndarray
        left_hand 2-element positional array
    np.ndarray
        right_foot 2-element positional array
    np.ndarray
        right_knee 2-element positional array
    np.ndarray
        left_knee 2-element positional array
    np.ndarray
        left_foot 2-element positional array
    """

    # -------------------
    # positions of points
    # -------------------
    right_hand = np.array([0 + posx, 413])
    right_elbow = np.array([45 + posx, 413])
    chest = np.array([90 + posx, 413])
    hips = np.array([90 + posx, 340])
    head = np.array([90 + posx, 470])
    left_elbow = np.array([135 + posx, 413])
    left_hand = np.array([180 + posx, 413])
    right_foot = np.array([20 + posx, 250])
    right_knee = np.array([45 + posx, 290])
    left_knee = np.array([135 + posx, 290])
    left_foot = np.array([160 + posx, 250])

    # ----------------
    # line connections
    # ----------------
    connectivity = [
        ["left_hand", "left_elbow"],
        ["left_elbow", "chest"],
        ["chest", "head"],
        ["chest", "right_elbow"],
        ["right_elbow", "right_hand"],
        ["chest", "hips"],
        ["hips", "left_knee"],
        ["left_knee", "left_foot"],
        ["hips", "right_knee"],
        ["right_knee", "right_foot"],
    ]

    # ----------------------------
    # read scene file if it exists
    # ----------------------------
    if os.path.exists(sceneName + ".json"):
        with open(sceneName + ".json", "r") as f:
            data = json.load(f)
        if "connections" not in data:
            data["connections"] = {}
    else:
        data = {"connections": {}}

    # -------------------------
    # write connections to data
    # -------------------------
    data["connections"][charName] = connectivity

    # -----------------------------
    # clear key times if they exist
    # -----------------------------
    data[charName] = {}

    # ------------------------
    # write data to scene file
    # ------------------------
    with open(sceneName + ".json", "w") as f:
        json.dump(data, f, indent="\t")

    return (
        right_hand,
        right_elbow,
        chest,
        hips,
        head,
        left_elbow,
        left_hand,
        right_foot,
        right_knee,
        left_knee,
        left_foot,
    )


def rotateLimb(p0: np.ndarray, p1: np.ndarray, rotation_angle: float) -> np.ndarray:
    """
    A function to rotate a single point `p1` around point `p0` by
    `rotation_angle`

    Parameters
    ----------
    p0 : np.ndarray
        stationary point
    p1 : np.ndarray
        rotating point
    rotation_angle : float
        angle of rotation in radians

    Returns
    -------
    np.ndarray
        new value of p1
    """
    rotation_mat = np.array([
        [np.cos(rotation_angle), -np.sin(rotation_angle)],
        [np.sin(rotation_angle), np.cos(rotation_angle)],
    ])
    relative_vector = p1 - p0
    return p0 + rotation_mat @ relative_vector


def writeTime(
    sceneName: str,
    charName: str,
    time: str,
    right_hand: np.ndarray,
    right_elbow: np.ndarray,
    chest: np.ndarray,
    hips: np.ndarray,
    head: np.ndarray,
    left_elbow: np.ndarray,
    left_hand: np.ndarray,
    right_foot: np.ndarray,
    right_knee: np.ndarray,
    left_knee: np.ndarray,
    left_foot: np.ndarray,
) -> None:
    """
    A function to write a character's points to a scene file

    Parameters
    ----------
    sceneName : str
        name of scene
    charName : str
        name of character
    time : str
        time to write to file
    right_hand : np.ndarray
        2-element ndarray for position of character right_hand
    right_elbow : np.ndarray
        2-element ndarray for position of character right_elbow
    chest : np.ndarray
        2-element ndarray for position of character chest
    hips : np.ndarray
        2-element ndarray for position of character hips
    head : np.ndarray
        2-element ndarray for position of character head
    left_elbow : np.ndarray
        2-element ndarray for position of character left_elbow
    left_hand : np.ndarray
        2-element ndarray for position of character left_hand
    right_foot : np.ndarray
        2-element ndarray for position of character right_foot
    right_knee : np.ndarray
        2-element ndarray for position of character right_knee
    left_knee : np.ndarray
        2-element ndarray for position of character left_knee
    left_foot : np.ndarray
        2-element ndarray for position of character left_foot
    """

    # ---------------
    # read scene file
    # ---------------
    with open(f"{sceneName}.json", "r") as f:
        data = json.load(f)

    # --------------------
    # add key time to data
    # --------------------
    if charName not in data:
        data[charName] = {}

    # ------------------------
    # update positions in data
    # ------------------------
    data[charName][time] = {
        "head": np.rint(head).astype(int).tolist(),
        "left_hand": np.rint(left_hand).astype(int).tolist(),
        "left_elbow": np.rint(left_elbow).astype(int).tolist(),
        "right_hand": np.rint(right_hand).astype(int).tolist(),
        "right_elbow": np.rint(right_elbow).astype(int).tolist(),
        "chest": np.rint(chest).astype(int).tolist(),
        "hips": np.rint(hips).astype(int).tolist(),
        "left_knee": np.rint(left_knee).astype(int).tolist(),
        "left_foot": np.rint(left_foot).astype(int).tolist(),
        "right_knee": np.rint(right_knee).astype(int).tolist(),
        "right_foot": np.rint(right_foot).astype(int).tolist(),
    }

    # ------------------------
    # write data to scene file
    # ------------------------
    with open(f"{sceneName}.json", "w") as f:
        json.dump(data, f, indent="\t")


class Render:
    def __init__(
        self,
        sceneName: str,
        size=(1080, 1920, 3),
        fps=30,
        displayCharNames=False,
    ) -> None:
        """
        Render an existing stick figure project file to an avi file

        Parameters
        ----------
        sceneName : str
            Name of scene json file and output video
        size : tuple, optional
            Resolution of Video, by default (1080, 1920, 3)
        fps : int, optional
            FPS of video, defaults to 30, by default 30
        displayCharNames : bool, optional
            Place Character names over their heads, by default False
        """

        # ------------------------------
        # assign arguments to attributes
        # ------------------------------
        self.__sceneName = sceneName
        self.__fps = fps
        self.__size = size
        self.__displayCharNames = displayCharNames

        # ---------------------
        # functional attributes
        # ---------------------
        self.__writer = None
        self.__charKeys = {}
        self.__charPoints = {}
        self.__time = 0.0
        self.__maxTime = 0.0
        self.__time_increment = 1.0 / self.__fps
        self.__lineThickness = 2
        self.__headRadius = 25
        self.__frame = None

        # ---------------
        # read scene file
        # ---------------
        with open(f"{sceneName}.json", "r") as f:
            self.__chars = json.load(f)
        self.__connections = self.__chars["connections"]
        self.__chars.pop("connections")

        # ----------------------------------
        # initialize dictionaries for frames
        # ----------------------------------
        self.__init_scene()

    def run(self) -> None:
        """
        Render scene to avi using OpenCV `VideoWriter`. Output file will
        be named `sceneName`.avi where `sceneName` is the value passed
        as the `sceneName` argument when initializating the `Render`
        instance.
        """

        # -------------------
        # define video writer
        # -------------------
        self.__writer = cv2.VideoWriter(
            f"{self.__sceneName}.avi",
            cv2.VideoWriter_fourcc(*"MJPG"),  # type: ignore
            self.__fps,
            (self.__size[1], self.__size[0]),
        )

        # -----------------------
        # loop through timestamps
        # -----------------------
        print("Rendering scene from json file")
        while self.__time < self.__maxTime:
            # print time update to terminal
            if self.__time:  # move cursor up one line and clear
                print("\033\\[1A", end="\x1b[2K")
            print(f"    Writing time: {round(self.__time, 1)} of {self.__maxTime}")

            # add next frame to video
            self.__interpolate_points()
            self.__draw_frame()
            self.__writer.write(self.__frame)  # type: ignore

            # increment
            self.__time += self.__time_increment

        print("Finished rendering project")
        self.__writer.release()

    def write_first_frame(self) -> None:
        """
        Write first frame of scene to jpg file. Output file will be
        named `sceneName`.jpg where `sceneName` is the value passed as
        the `sceneName` argument when initializating the `Render`
        instance.
        """

        self.__interpolate_points()
        self.__draw_frame()
        cv2.imwrite(f"{self.__sceneName}.jpg", self.__frame)  # type: ignore

    def show_first_frame(self) -> None:
        """
        Display first frame of scene using OpenCV
        """

        self.__interpolate_points()
        self.__draw_frame()
        cv2.imshow(self.__sceneName, self.__frame)  # type: ignore
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __init_scene(self) -> None:
        """
        Initialize scene dictionaries
        """

        for char in self.__chars:
            self.__charKeys[char] = np.array(list(self.__chars[char].keys()), dtype=float)
            self.__maxTime = max(self.__maxTime, max(self.__charKeys[char]))
            self.__charPoints[char] = self.__chars[char][str(self.__time)]

    def __interpolate_points(self) -> None:
        """
        interpolate character points at the next frame time
        """

        # -----------------------------------
        # loop through chars and reset points
        # -----------------------------------
        for char in self.__chars:
            # --------------------------
            # self.time == char key time
            # --------------------------
            if str(self.__time) in self.__chars[char]:
                self.__charPoints[char] = self.__chars[char][str(self.__time)]

            # -----------------------------
            # self.time > max time for char
            # -----------------------------
            elif self.__time > max(self.__charKeys[char]):
                pass

            # ----------------------
            # interpolate each point
            # ----------------------
            else:
                ind = np.searchsorted(self.__charKeys[char], self.__time)
                t0 = self.__charKeys[char][ind - 1]
                t1 = self.__charKeys[char][ind]
                t_ratio = (self.__time - t0) / (t1 - t0)
                for point in self.__charPoints[char]:
                    p0 = self.__chars[char][str(float(t0))][point]
                    p1 = self.__chars[char][str(float(t1))][point]
                    self.__charPoints[char][point][0] = int(p0[0] + t_ratio * (p1[0] - p0[0]))
                    self.__charPoints[char][point][1] = int(p0[1] + t_ratio * (p1[1] - p0[1]))

    def __draw_frame(self) -> None:
        """
        Draw character bodies to image frame
        """

        # -------------------------------
        # reset frame to white background
        # -------------------------------
        self.__frame = self.__frame = np.ones(self.__size, np.uint8) * 255

        # -------------------
        # draw chars on frame
        # -------------------
        for char in self.__chars:
            # ---------
            # draw head
            # ---------
            posx, posy = self.__charPoints[char]["head"]
            self.__frame = cv2.circle(
                self.__frame,
                (int(posx), int(posy)),
                self.__headRadius,
                (0, 0, 0),
                self.__lineThickness,
            )

            # --------------------------
            # draw char names over heads
            # --------------------------
            if self.__displayCharNames:
                self.__frame = cv2.putText(
                    self.__frame,
                    char,
                    (posx - 45, posy + 45),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 0),
                    self.__lineThickness,
                    bottomLeftOrigin=True,
                )

            # ---------
            # draw body
            # ---------
            for line in self.__connections[char]:
                p0 = self.__charPoints[char][line[0]]
                p1 = self.__charPoints[char][line[1]]
                p0_1_0 = p0[1]
                p1_1_0 = p1[1]
                if line[0] == "head":
                    p0[1] -= self.__headRadius
                elif line[1] == "head":
                    p1[1] -= self.__headRadius
                self.__frame = cv2.line(self.__frame, p0, p1, (0, 0, 0), self.__lineThickness)
                self.__charPoints[char][line[0]][1] = p0_1_0
                self.__charPoints[char][line[1]][1] = p1_1_0

        # ----------
        # flip frame
        # ----------
        self.__frame = np.flip(self.__frame, axis=0)
