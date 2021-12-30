def IOU(dA, dB):
    xA, yA, wA, hA, pA = dA
    xB, yB, wB, hB, pB = dB

    minBottomSide = min(yA + hA, yB + hB)
    maxTopSide    = max(yA, yB)
    overlapRow    = max(0, minBottomSide - maxTopSide)

    minRightSide  = min(xA + wA, xB + wB)
    maxLeftSide   = max(xA, xB)
    overlapCol    = max(0, minRightSide - maxLeftSide)

    overlapArea   = overlapRow * overlapCol
    totalArea     = wA * hA + wB * hB - overlapArea
    return overlapArea / totalArea


def markOverlaps(labels, idx, detections):
    for i in range(len(detections)):
        if labels[i] == 0 and IOU(detections[idx], detections[i]) > 0.5:
            labels[i] = labels[idx]
            markOverlaps(labels, i, detections)


def getClusterLabels(labels, detections):
    count = 0
    for i in range(len(detections)):
        if labels[i] == 0:
            labels[i] = count + 1
            markOverlaps(labels, i, detections)
            count += 1

    return count


def getCluster(detections, labels, label):
    xCr, yCr, wr, hr, probR = 0, 0, 0, 0, 0

    nDetectionsInCluster = 0
    for i in range(0, len(detections)):
        if labels[i] != label: continue
        x, y, w, h, p = detections[i]

        xCr   += x + w/2
        yCr   += y + h/2
        wr    += w
        hr    += h
        probR += p

        nDetectionsInCluster += 1

    xCr /= nDetectionsInCluster
    yCr /= nDetectionsInCluster
    wr  /= nDetectionsInCluster
    hr  /= nDetectionsInCluster

    return [xCr - wr/2, yCr - hr/2, wr, hr, probR]


def clusterDetections(detections, minConf = 10):
    labels = [0] * len(detections)
    count = getClusterLabels(labels, detections)

    rDetections = []
    for cIdx in range(1, count+1):
        rDetection = getCluster(detections, labels, cIdx)
        if rDetection[-1] >= minConf:
            rDetections.append(rDetection)

    return rDetections

