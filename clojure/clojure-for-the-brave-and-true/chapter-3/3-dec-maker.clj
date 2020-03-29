(defn dec-maker
  "Write a function, dec-maker,
  that works exactly like the function inc-maker except with subtraction:

  (def dec9 (dec-maker 9))
  (dec9 10)
  ; => 1"

  [v]
  (fn [num] (- num v)))


(do
    (println ((dec-maker 9) 10))
    (println ((dec-maker 1) 10))
    (println ((dec-maker 10) 0)))
