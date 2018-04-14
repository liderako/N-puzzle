package ru.dokwork.algorithms.astar;

import java.util.*;

/**
 * Реализует алгоритм поиска решения А*.
 */
public class Astar<TState extends State, TRules extends Rules<TState>> {

    /**
     * Применяет алгоритм А* для поиска крадчайшего пути до терминального
     * состоянияот указанного.
     *
     * @param startState - начальное состояние.
     * @return последовательность состояний от заданного до терминального.
     */
    public Collection<State> search(TState startState) {
        LinkedList<Integer> close = new LinkedList<Integer>();
        LinkedList<TState> open = new LinkedList<TState>();
        open.add(startState);
        startState.setG(0);
        startState.setH(rules.getH(startState));

        while (!open.isEmpty()) {

            TState x = getStateWithMinF(open);
           
            if (rules.isTerminate(x)) {
                closedStates = close.size();
                return completeSolution(x);
            }

            open.remove(x);
            close.add(x.hashCode());

            List<TState> neighbors = rules.getNeighbors(x);
            
            for (TState neighbor : neighbors) {
                if (close.contains(neighbor.hashCode())) {
                    continue;
                }
                int g = x.getG() + rules.getDistance(x, neighbor);
                boolean isGBetter;

                if (!open.contains(neighbor)) {
                    neighbor.setH(rules.getH(neighbor));
                    open.add(neighbor);
                    isGBetter = true;
                } else {
                    isGBetter = g < neighbor.getG();
                }
                if (isGBetter) {
                    neighbor.setParent(x);
                    neighbor.setG(g);
                }
            }

        }
        return null;
    }

    public int getClosedStatesCount() {
        return closedStates;
    }

    /**
     * Создает объект для поиска терминального состояния по указанным правилам.
     *
     * @param rules правила, в соответствии с которыми будет производиться поиск
     *              терминального состояния.
     */
    public Astar(TRules rules) {
        if (rules == null) {
            throw new IllegalArgumentException("Rules can`t be null.");
        }
        this.rules = rules;
    }

    /**
     * Находит вершину в списке open с наименьшим значением веса.
     *
     * @param open список открытых вершин.
     * @return вершину с наименьшим весом.
     */
    private TState getStateWithMinF(Collection<TState> open) {
        TState res = null;
        int min = Integer.MAX_VALUE;
        for (TState state : open) {
            if (state.getF() < min) {
                min = state.getF();
                res = state;
            }
        }
        return res;
    }

    /**
     * Составляет последовательность состояний пройденных от начального
     * состояния до конечного.
     *
     * @param terminate найденное конечное состояние.
     * @return последовательность состояний пройденных от начального
     * состояния до конечного.
     */
    private Collection<State> completeSolution(TState terminate) {
        LinkedList<State> path = new LinkedList<State>();
        State c = terminate;
        while (c != null) {
            path.addFirst(c);
            c = c.getParent();
        }
        return path;
    }

    private TRules rules;
    private int closedStates = 0;
}


















public static List<Point> FindPath(int[,] field, Point start, Point goal)
{
  // Шаг 1.
  var closedSet = new Collection<PathNode>();
  var openSet = new Collection<PathNode>();
  // Шаг 2.
  PathNode startNode = new PathNode()
  {
    Position = start,
    CameFrom = null,
    PathLengthFromStart = 0,
    HeuristicEstimatePathLength = GetHeuristicPathLength(start, goal)
  };

  openSet.Add(startNode);
  while (openSet.Count > 0)
  {
    // Шаг 3.
    var currentNode = openSet.OrderBy(node => 
      node.EstimateFullPathLength).First();
    // Шаг 4.
    if (currentNode.Position == goal)
      return GetPathForNode(currentNode);


    // Шаг 5.
    openSet.Remove(currentNode);
    closedSet.Add(currentNode);


    // Шаг 6.
    foreach (var neighbourNode in GetNeighbours(currentNode, goal, field))
    {
      // Шаг 7.
      if (closedSet.Count(node => node.Position == neighbourNode.Position) > 0)
        continue;
     

     var openNode = openSet.FirstOrDefault(node => node.Position == neighbourNode.Position);
      // Шаг 8.
      if (openNode == null)
        openSet.Add(neighbourNode);
      else
        if (openNode.PathLengthFromStart > neighbourNode.PathLengthFromStart)
        {
          // Шаг 9.
          openNode.CameFrom = currentNode;
          openNode.PathLengthFromStart = neighbourNode.PathLengthFromStart;
        }
    }
  }
  // Шаг 10.
  return null;
}
