// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract BoxV2 {

    uint256 private value;

    event valueChanged(uint256 newValue);

    function store(uint256 newValue) public {
        value = newValue;
        emit valueChanged(newValue);
    }

    function retrieve() public view returns (uint256){
        return value;
    }

    function increment() public {
        value++;
        emit valueChanged(value);
    }

}