package ru.dokwork.algorithms.astar;

import java.util.List;

/**
 * Определяет специфичные для задачи правила ее решения.
 * 
 * @author: dok
 */
public interface Rules<TState extends State> {

	/**
	 * Возвращает список состояний, в которые может быть осуществлен переход из
	 * указанного состояния.
	 * 
	 * @param currentState
	 *            текущее состояние, для которого раскрываются соседние.
	 * @return список состояний, в которые может быть осуществлен переход из
	 *         указанного состояния.
	 */
	List<TState> getNeighbors(TState currentState);

	/**
	 * Возвращает растояние между указанными состояниями.
	 * 
	 * @param a
	 *            первое состояние.
	 * @param b
	 *            второе состояние.
	 * @return растояние между указанными состояниями.
	 */
	int getDistance(TState a, TState b);

	/**
	 * Вычисляет эвристическую оценку расстояния от указанного состояния до
	 * конечного.
	 * 
	 * @param state
	 *            текущее состояние.
	 * @return значение оценки расстояния от указанного состояния до конечного.
	 */
	int getH(TState state);

	/**
	 *  
	 * 
	 * @param state
	 *            состояние.
	 * @return true, если состояние конечное.
	 */
	boolean isTerminate(TState state);
}