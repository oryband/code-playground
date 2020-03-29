(defn mapset
  "Write a function, mapset, that works like map except the return value is a set:

  (mapset inc [1 1 2 2])
  ; => #{2 3}"

  [f coll]

  (loop [remaining coll
         res #{}]
    (if (empty? remaining)
      res
      (let [[x & xs] remaining]
        (recur xs
               (conj res (f x)))))))


(do
    (println (mapset inc [1 1 1 1 2 2 2 3])))
